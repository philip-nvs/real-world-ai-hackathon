import type { ReactNode } from 'react'

type Block = { kind: 'h' | 'li' | 'q' | 'p'; lines: string[] }

// Renders only the markdown subset write_answer in src/agent/core.py emits:
// ## headings, "- " lists, "> " quotes, paragraphs, **bold** and `code`.
export function Markdown({ text }: { text: string }) {
  const blocks: (Block | null)[] = []
  for (const line of text.split('\n')) {
    const kind = line.startsWith('#') ? 'h' : line.startsWith('- ') ? 'li' : line.startsWith('>') ? 'q' : line.trim() ? 'p' : null
    const last = blocks.at(-1)
    if (kind && last?.kind === kind && kind !== 'h') last.lines.push(line)
    else blocks.push(kind && { kind, lines: [line] })
  }
  return <div className="space-y-3 leading-relaxed">{blocks.map((b, i) => b && <BlockView key={i} b={b} />)}</div>
}

function BlockView({ b }: { b: Block }) {
  switch (b.kind) {
    case 'h':
      return (
        <h4 className="pt-3 text-xs font-semibold tracking-wide text-muted-foreground uppercase first:pt-0">
          {b.lines[0].replace(/^#+\s*/, '')}
        </h4>
      )
    case 'li':
      return (
        <ul className="list-disc space-y-1 pl-5 marker:text-muted-foreground">
          {b.lines.map((l, i) => <li key={i}>{inline(l.slice(2))}</li>)}
        </ul>
      )
    case 'q':
      return (
        <blockquote className="space-y-2 rounded-r border-l-2 border-primary/40 bg-muted/50 px-3 py-2">
          {b.lines.map((l) => l.replace(/^>\s?/, '')).join('\n').split(/\n{2,}/).map((p, i) => (
            <p key={i} className="whitespace-pre-wrap">{inline(p)}</p>
          ))}
        </blockquote>
      )
    case 'p':
      return <p className="whitespace-pre-wrap">{inline(b.lines.join('\n'))}</p>
  }
}

const inline = (s: string): ReactNode[] =>
  s.split(/(\*\*[^*]+\*\*|`[^`]+`)/).map((part, i) =>
    part.startsWith('**') && part.endsWith('**') && part.length > 4 ? (
      <strong key={i} className="font-semibold">{part.slice(2, -2)}</strong>
    ) : part.startsWith('`') && part.endsWith('`') && part.length > 2 ? (
      <code key={i} className="rounded bg-muted px-1 py-0.5 font-mono text-[0.85em]">{part.slice(1, -1)}</code>
    ) : (
      part
    ),
  )
