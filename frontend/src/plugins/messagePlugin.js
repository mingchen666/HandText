import { Message } from './messageManager'

export default function createMessagePlugin() {
  return {
    install(App) {
      App.config.globalProperties.$message = Message
    }
  }
}
