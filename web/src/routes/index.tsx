import { useEffect, useRef, useState, type DragEvent } from 'react'
import { createFileRoute } from '@tanstack/react-router'
import { useQueryClient } from '@tanstack/react-query'
import { ChevronRightIcon, DownloadIcon, FileIcon, FolderUpIcon, PlayIcon, RotateCwIcon, Trash2Icon, UploadIcon, XIcon } from 'lucide-react'
import { cn } from 'cn'
import { api, errorMessage } from '@/api/client'
import type { components } from '@/api/schema'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'

export const Route = createFileRoute('/')({ component: Index })

type Entry = { path: string; file: File }

const fromFiles = (files: FileList | null): Entry[] =>
  Array.from(files ?? [], (file) => ({ path: file.webkitRelativePath || file.name, file }))

// Dropped folders only come through the entries API, so walk it.
async function walk(entry: FileSystemEntry): Promise<Entry[]> {
  if (entry.isFile) {
    const file = await new Promise<File>((res, rej) => (entry as FileSystemFileEntry).file(res, rej))
    return [{ path: entry.fullPath.replace(/^\//, ''), file }]
  }
  const reader = (entry as FileSystemDirectoryEntry).createReader()
  const children: FileSystemEntry[] = []
  for (;;) {
    const batch = await new Promise<FileSystemEntry[]>((res, rej) => reader.readEntries(res, rej))
    if (!batch.length) break
    children.push(...batch)
  }
  return (await Promise.all(children.map(walk))).flat()
}

const formatSize = (bytes: number) =>
  bytes < 1024 ? `${bytes} B` : bytes < 1024 ** 2 ? `${(bytes / 1024).toFixed(1)} KB` : `${(bytes / 1024 ** 2).toFixed(1)} MB`

function Index() {
  const [entries, setEntries] = useState<Entry[]>([])
  const [dragging, setDragging] = useState(false)
  const [caseId, setCaseId] = useState('')
  // Bumped by "Play all"; every row starts a session when it changes.
  const [playAll, setPlayAll] = useState(0)
  const [exportError, setExportError] = useState('')
  const fileInput = useRef<HTMLInputElement>(null)
  const folderInput = useRef<HTMLInputElement>(null)

  const queryClient = useQueryClient()
  const refreshCases = () => queryClient.invalidateQueries({ queryKey: api.queryOptions('get', '/cases').queryKey })
  const cases = api.useQuery('get', '/cases')
  const remove = api.useMutation('delete', '/cases/{case_id}', { onSuccess: refreshCases })
  const uploadCase = api.useMutation('post', '/cases', {
    onSuccess: () => (setEntries([]), setCaseId(''), refreshCases()),
  })
  const uploading = uploadCase.isPending

  const add = (next: Entry[]) => {
    uploadCase.reset()
    setEntries((prev) => {
      const byPath = new Map(prev.map((e) => [e.path, e]))
      for (const e of next) byPath.set(e.path, e)
      return [...byPath.values()].sort((a, b) => a.path.localeCompare(b.path))
    })
  }

  const onDrop = async (e: DragEvent) => {
    e.preventDefault()
    setDragging(false)
    const roots = Array.from(e.dataTransfer.items, (i) => i.webkitGetAsEntry()).filter((x) => x !== null)
    add((await Promise.all(roots.map(walk))).flat())
  }

  const upload = () => {
    // Each part's filename is its path inside the case; openapi-fetch sends FormData as-is.
    const body = new FormData()
    for (const { path, file } of entries) body.append('files', file, path)
    if (caseId.trim()) body.append('case_id', caseId.trim())
    uploadCase.mutate({ body: body as never })
  }

  // fetch rather than a plain link so a 404 shows here instead of downloading as a broken file
  const exportAnswers = async () => {
    setExportError('')
    const res = await fetch(`/api/export?${new URLSearchParams(cases.data?.map((c) => ['case_id', c.id]))}`)
    if (!res.ok) return setExportError(errorMessage(await res.json().catch(() => res.statusText)))
    const a = document.createElement('a')
    a.href = URL.createObjectURL(await res.blob())
    a.download = 'ANSWERS.zip'
    a.click()
    URL.revokeObjectURL(a.href)
  }

  const total = entries.reduce((n, e) => n + e.file.size, 0)

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4 bg-muted/30 p-4">
      <Card className="w-full max-w-lg">
        <CardHeader>
          <CardTitle>Upload a case</CardTitle>
          <CardDescription>A case folder (with its index.md, history.md and attachments) or individual files.</CardDescription>
        </CardHeader>

        <CardContent className="space-y-4">
          <div
            onDragOver={(e) => {
              e.preventDefault()
              setDragging(true)
            }}
            onDragLeave={() => setDragging(false)}
            onDrop={onDrop}
            className={cn(
              'flex flex-col items-center gap-3 rounded-lg border border-dashed px-6 py-10 text-center transition-colors',
              dragging ? 'border-primary bg-primary/5' : 'border-border',
            )}
          >
            <UploadIcon className="size-6 text-muted-foreground" />
            <p className="text-sm text-muted-foreground">Drop a folder or files here</p>
            <div className="flex gap-2">
              <Button variant="outline" size="sm" onClick={() => folderInput.current?.click()}>
                <FolderUpIcon /> Choose folder
              </Button>
              <Button variant="outline" size="sm" onClick={() => fileInput.current?.click()}>
                <FileIcon /> Choose files
              </Button>
            </div>
            <input
              ref={folderInput}
              type="file"
              hidden
              // @ts-expect-error non-standard but supported by every major browser
              webkitdirectory=""
              onChange={(e) => (add(fromFiles(e.target.files)), (e.target.value = ''))}
            />
            <input
              ref={fileInput}
              type="file"
              hidden
              multiple
              onChange={(e) => (add(fromFiles(e.target.files)), (e.target.value = ''))}
            />
          </div>

          {entries.length > 0 && (
            <ul className="max-h-64 divide-y overflow-y-auto rounded-lg border text-sm">
              {entries.map(({ path, file }) => (
                <li key={path} className="flex items-center gap-3 px-3 py-2">
                  <span className="min-w-0 flex-1 truncate font-mono text-xs" title={path}>
                    {path}
                  </span>
                  <span className="shrink-0 text-xs text-muted-foreground tabular-nums">{formatSize(file.size)}</span>
                  <Button
                    variant="ghost"
                    size="icon-xs"
                    aria-label={`Remove ${path}`}
                    onClick={() => setEntries((prev) => prev.filter((e) => e.path !== path))}
                  >
                    <XIcon />
                  </Button>
                </li>
              ))}
            </ul>
          )}

          <label className="block space-y-1 text-sm">
            <span className="text-muted-foreground">Case id (optional for a single folder)</span>
            <input
              value={caseId}
              onChange={(e) => setCaseId(e.target.value)}
              placeholder="Defaults to the folder name"
              className="w-full rounded-md border bg-background px-3 py-1.5 text-sm outline-none focus-visible:ring-2 focus-visible:ring-ring"
            />
          </label>

          {uploadCase.isSuccess && (
            <p className="text-sm text-muted-foreground">
              Uploaded case <span className="font-mono">{uploadCase.data.id}</span> ({uploadCase.data.files.length} files).
            </p>
          )}
          {uploadCase.isError && <p className="text-sm text-destructive">Upload failed: {errorMessage(uploadCase.error)}</p>}
        </CardContent>

        <CardFooter className="justify-between gap-2">
          <span className="text-xs text-muted-foreground">
            {entries.length ? `${entries.length} file${entries.length > 1 ? 's' : ''} · ${formatSize(total)}` : 'Nothing selected'}
          </span>
          <div className="flex gap-2">
            <Button variant="ghost" disabled={!entries.length || uploading} onClick={() => setEntries([])}>
              Clear
            </Button>
            <Button disabled={!entries.length || uploading} onClick={upload}>
              {uploading ? 'Uploading…' : 'Upload'}
            </Button>
          </div>
        </CardFooter>
      </Card>

      <Card className="w-full max-w-lg">
        <CardHeader className="flex flex-row items-center justify-between">
          <CardTitle>Cases</CardTitle>
          <div className="flex gap-2">
            <Button variant="outline" size="sm" disabled={!cases.data?.length} onClick={exportAnswers}>
              <DownloadIcon /> Export all
            </Button>
            <Button variant="outline" size="sm" disabled={!cases.data?.length} onClick={() => setPlayAll((n) => n + 1)}>
              <PlayIcon /> Play all
            </Button>
          </div>
        </CardHeader>
        <CardContent className="text-sm">
          {cases.isPending && <p className="text-muted-foreground">Loading…</p>}
          {cases.isError && <p className="text-destructive">Couldn't load cases: {errorMessage(cases.error)}</p>}
          {cases.data?.length === 0 && <p className="text-muted-foreground">No cases yet.</p>}
          {!!cases.data?.length && (
            <ul className="divide-y rounded-lg border">
              {cases.data.map((c) => (
                <CaseRow
                  key={c.id}
                  id={c.id}
                  uploadedAt={c.uploaded_at}
                  deleting={remove.isPending}
                  playAll={playAll}
                  onDelete={() => confirm(`Delete case ${c.id}?`) && remove.mutate({ params: { path: { case_id: c.id } } })}
                />
              ))}
            </ul>
          )}
          {remove.isError && <p className="mt-2 text-destructive">Delete failed: {errorMessage(remove.error)}</p>}
          {exportError && <p className="mt-2 text-destructive">Export failed: {exportError}</p>}
        </CardContent>
      </Card>
    </main>
  )
}

type CaseRowProps = {
  id: string
  uploadedAt: string
  deleting: boolean
  playAll: number
  onDelete: () => void
}

// Expands to the case's files; they're only fetched once the row is opened.
function CaseRow({ id, uploadedAt, deleting, playAll, onDelete }: CaseRowProps) {
  const [open, setOpen] = useState(false)
  const detail = api.useQuery('get', '/cases/{case_id}', { params: { path: { case_id: id } } }, { enabled: open })
  const start = api.useMutation('post', '/cases/{case_id}/sessions', { onSettled: () => setOpen(true) })
  // Polls the latest run until it ends.
  const session = api.useQuery(
    'get',
    '/sessions/{session_id}',
    { params: { path: { session_id: start.data?.id ?? '' } } },
    { enabled: !!start.data, refetchInterval: (q) => (finished(q.state.data?.status) ? false : 1000) },
  )
  const past = api.useQuery('get', '/cases/{case_id}/sessions', { params: { path: { case_id: id } } })
  const ran = !!start.data || !!past.data?.length
  const running = start.isPending || (!!start.data && !finished(session.data?.status))
  const play = () => start.mutate({ params: { path: { case_id: id } } })
  // Skips mount (0) and rows already running.
  useEffect(() => {
    if (playAll && !running) play()
  }, [playAll]) // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <li>
      <details className="group" open={open} onToggle={(e) => setOpen(e.currentTarget.open)}>
        <summary className="flex cursor-pointer list-none items-center gap-3 px-3 py-2 hover:bg-muted/50">
          <ChevronRightIcon className="size-4 shrink-0 text-muted-foreground transition-transform group-open:rotate-90" />
          <span className="min-w-0 flex-1 truncate font-mono text-xs">{id}</span>
          <span className="shrink-0 text-xs text-muted-foreground">{new Date(uploadedAt).toLocaleString()}</span>
          <Button
            variant="ghost"
            size="icon-xs"
            aria-label={`${ran ? 'Re-run' : 'Start'} a session on case ${id}`}
            title={ran ? 'Re-run' : 'Run'}
            disabled={running}
            onClick={(e) => (e.preventDefault(), play())}
          >
            {ran ? <RotateCwIcon /> : <PlayIcon />}
          </Button>
          <Button
            variant="ghost"
            size="icon-xs"
            aria-label={`Delete case ${id}`}
            disabled={deleting}
            // keep the click from also toggling the row
            onClick={(e) => (e.preventDefault(), onDelete())}
          >
            <Trash2Icon />
          </Button>
        </summary>
        <div className="border-t bg-muted/20 px-3 py-2">
          {detail.isPending && <p className="text-muted-foreground">Loading…</p>}
          {detail.isError && <p className="text-destructive">Couldn't load files: {errorMessage(detail.error)}</p>}
          {detail.data && (
            <ul className="space-y-1">
              {detail.data.files.map((f) => (
                <li key={f.path} className="flex items-center gap-3 pl-7">
                  <FileIcon className="size-3.5 shrink-0 text-muted-foreground" />
                  <a
                    // the API takes the path with its "/" unescaped
                    href={`/api/cases/${encodeURIComponent(id)}/files/${f.path.split('/').map(encodeURIComponent).join('/')}`}
                    target="_blank"
                    rel="noreferrer"
                    className="min-w-0 flex-1 truncate font-mono text-xs hover:underline"
                    title={f.path}
                  >
                    {f.path}
                  </a>
                  <span className="shrink-0 text-xs text-muted-foreground tabular-nums">{formatSize(f.size)}</span>
                </li>
              ))}
            </ul>
          )}
          {start.isError && <p className="mt-2 text-destructive">Couldn't start a session: {errorMessage(start.error)}</p>}
          {start.data && <SessionTrace key={start.data.id} sessionId={start.data.id} session={session.data} />}
        </div>
      </details>
    </li>
  )
}

type SessionEvent = components['schemas']['SessionEvent']
const finished = (status?: string) => status === 'done' || status === 'failed'
const json = (v: unknown) => JSON.stringify(v, null, 2)

// Polls the trace until the run ends. A done session's last trace line is always its decision,
// so this stops on that (or on failed), never before its final lines are in.
// ponytail: refetches the whole trace each second; pass `after` and append if traces grow long
function SessionTrace({ sessionId, session }: { sessionId: string; session?: components['schemas']['Session'] }) {
  const events = api.useQuery(
    'get',
    '/sessions/{session_id}/events',
    { params: { path: { session_id: sessionId } } },
    { refetchInterval: (q) => (q.state.data?.at(-1)?.kind === 'decision' || session?.status === 'failed' ? false : 1000) },
  )
  const status = session?.status ?? 'queued'

  return (
    <div className="mt-3 space-y-2 border-t pt-3">
      <p className="text-xs text-muted-foreground">
        Session <span className="font-mono">{sessionId.slice(0, 8)}</span> · {status}
        {!finished(status) && '…'}
      </p>
      {session?.error && <p className="text-xs text-destructive">{session.error}</p>}
      <ol className="max-h-96 space-y-2 overflow-y-auto text-xs">
        {events.data?.map((e) => (
          <li key={e.seq}>
            <TraceLine e={e} />
          </li>
        ))}
      </ol>
    </div>
  )
}

const pre = 'max-h-40 overflow-auto whitespace-pre-wrap rounded bg-muted p-2 font-mono text-[11px]'

function TraceLine({ e }: { e: SessionEvent }) {
  const d = e as Record<string, any>
  switch (e.kind) {
    case 'loaded':
      return <p className="text-muted-foreground">Loaded {d.case}: {d.events} events, {d.attachments.length} attachments</p>
    case 'model':
      return (
        <div className="space-y-1">
          {d.thinking?.map((t: string, i: number) => (
            <p key={i} className="whitespace-pre-wrap text-muted-foreground italic">{t}</p>
          ))}
          {d.text.map((t: string, i: number) => (
            <p key={i} className="whitespace-pre-wrap">{t}</p>
          ))}
        </div>
      )
    case 'tool_call':
      return (
        <div>
          <p className="font-mono">→ {d.tool}</p>
          <pre className={pre}>{json(d.input)}</pre>
        </div>
      )
    case 'tool_result':
      return (
        <div>
          <p className="font-mono text-muted-foreground">← {d.tool}</p>
          <pre className={pre}>{json(d.output)}</pre>
        </div>
      )
    case 'tool_error':
      return <p className="font-mono text-destructive">✕ {d.tool}: {d.error}</p>
    case 'guard_block':
      return <p className="font-mono text-destructive">⛔ {d.tool} blocked: {d.problems.join('; ')}</p>
    case 'crash':
      return <p className="font-mono text-destructive">Crashed: {d.error}</p>
    case 'decision':
      return (
        <p className="rounded border p-2">
          <span className="font-medium uppercase">{d.decision}</span> · {d.final_result}
        </p>
      )
  }
}
