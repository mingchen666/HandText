// 手写转文本
import request from '@/utils/request'
export const generateWrite2TextService = (formData) => {
  return request({
    url: '/api/write/to/text',
    method: 'post',
    data: formData
  })
}