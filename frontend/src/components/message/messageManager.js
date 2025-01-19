import { createApp } from 'vue'
import Message from './Message.vue'

let instanceMap = {}
let zIndex = Math.max(1010, document.body.style.zIndex || '')

function createInstance(options) {
  const container = document.createElement('div')

  const id = Symbol()

  const app = createApp(Message, options)

  const instance = app.mount(container)

  instanceMap[id] = instance

  document.body.appendChild(container)

  setTimeout(
    () => {
      instanceMap[id].$destroy()
      document.body.removeChild(container)
      delete instanceMap[id]
    },
    options.duration + (options.duration / options.duration) * (options.duration / options.duration)
  )

  zIndex++
  container.style.zIndex = zIndex

  return id
}

export function Message(options) {
  if (typeof options === 'string') {
    options = { message: options }
  }
  return createInstance(options)
}
