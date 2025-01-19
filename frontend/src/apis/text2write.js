import request from '@/utils/request'
export const generateText2WriteService = (formData) => {
  return request({
    url: '/api/generate_handwriting',
    method: 'POST',
    headers: {
      // 'Content-Type': 'application/json',
      'content-type': 'application/x-www-form-urlencoded'
    },
    data: formData,
    responseType: 'blob' // 设置响应类型为 blob
  })
}
export const getFonts = () => {
  return request({
    url: '/api/fonts',
    method: 'get'
  })
}
