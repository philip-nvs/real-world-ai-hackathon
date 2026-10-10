import { useRef, useState, type DragEvent } from 'react'
import { createFileRoute } from '@tanstack/react-router'
import { FileIcon, FolderUpIcon, UploadIcon, XIcon } from 'lucide-react'
import { cn } from 'cn'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'

export const Route = createFileRoute('/')({ component: Index })

// ponytail: endpoint TBC; files go up as one multipart form, field "files", filename = path inside the case
const UPLOAD_URL = '/api/cases/upload'

type Entry = { path: string; file: File }
type Status = { kind: 'idle' | 'uploading' | 'done' } | { kind: 'error'; message: string }

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
  const [status, setStatus] = useState<Status>({ kind: 'idle' })
  const fileInput = useRef<HTMLInputElement>(null)
  const folderInput = useRef<HTMLInputElement>(null)

  const add = (next: Entry[]) => {
    setStatus({ kind: 'idle' })
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

  const upload = async () => {
    setStatus({ kind: 'uploading' })
    const body = new FormData()
    for (const { path, file } of entries) body.append('files', file, path)
    try {
      const res = await fetch(UPLOAD_URL, { method: 'POST', body })
      if (!res.ok) throw new Error(`${res.status} ${res.statusText}`)
      setStatus({ kind: 'done' })
      setEntries([])
    } catch (err) {
      setStatus({ kind: 'error', message: err instanceof Error ? err.message : String(err) })
    }
  }

  const total = entries.reduce((n, e) => n + e.file.size, 0)

  return (
    <main className="flex min-h-screen items-center justify-center bg-muted/30 p-4">
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

          {status.kind === 'done' && <p className="text-sm text-muted-foreground">Uploaded.</p>}
          {status.kind === 'error' && <p className="text-sm text-destructive">Upload failed: {status.message}</p>}
        </CardContent>

        <CardFooter className="justify-between gap-2">
          <span className="text-xs text-muted-foreground">
            {entries.length ? `${entries.length} file${entries.length > 1 ? 's' : ''} · ${formatSize(total)}` : 'Nothing selected'}
          </span>
          <div className="flex gap-2">
            <Button variant="ghost" disabled={!entries.length || status.kind === 'uploading'} onClick={() => setEntries([])}>
              Clear
            </Button>
            <Button disabled={!entries.length || status.kind === 'uploading'} onClick={upload}>
              {status.kind === 'uploading' ? 'Uploading…' : 'Upload'}
            </Button>
          </div>
        </CardFooter>
      </Card>
    </main>
  )
}
