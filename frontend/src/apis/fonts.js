import request from '@/utils/request'
export const getImg = (data) => {
  return request({
    url: '/api/img',
    method: 'post',
    data
  })
}
