// 字符串转换成计算公式

// 普通对象转换成表单对象(包含二进制)
export function objectToFormData(obj, fileState) {
  const formData = new FormData()

  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      let value = obj[key]

      if (value instanceof ArrayBuffer) {
        // 使用 fileState 中对应的文件类型
        const mimeType = fileState.file.type
        value = new Blob([value], { type: mimeType })
      }

      if (value instanceof Blob || value instanceof File) {
        // 如果是 Blob 或 File 对象，直接添加，并指定文件名（如果有的话）
        formData.append(key, value, value.name || key)
      } else {
        // 默认情况下，添加普通值
        formData.append(key, value)
      }
    }
  }
  return formData
}
// 可选第二个参数
export function objectToFormData2(obj, fileState = null) {
  const formData = new FormData()

  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      let value = obj[key]

      if (value instanceof ArrayBuffer) {
        let mimeType = 'application/octet-stream' // 默认 MIME 类型
        if (fileState && fileState.file && fileState.file.type) {
          mimeType = fileState.file.type
        }
        value = new Blob([value], { type: mimeType })
      }

      if (value instanceof Blob || value instanceof File) {
        // 如果是 Blob 或 File 对象，直接添加，并指定文件名（如果有的话）
        formData.append(key, value, value.name || key)
      } else {
        // 默认情况下，添加普通值
        formData.append(key, value)
      }
    }
  }
  return formData
}
