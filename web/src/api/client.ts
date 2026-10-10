import createFetchClient from 'openapi-fetch'
import createClient from 'openapi-react-query'
import type { paths } from './schema'

// Vite proxies /api to the FastAPI server (see vite.config.ts).
export const fetchClient = createFetchClient<paths>({ baseUrl: '/api' })
export const api = createClient(fetchClient)

// FastAPI errors are { detail: string | validation-error[] }.
export const errorMessage = (err: unknown) => {
  const detail = (err as { detail?: unknown } | null)?.detail
  if (typeof detail === 'string') return detail
  if (detail) return JSON.stringify(detail)
  return err instanceof Error ? err.message : String(err)
}
