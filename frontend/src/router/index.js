import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/home/index.vue'
import Layout from '@/layout/index.vue'
import Write from '@/views/text2write/index.vue'
import TextWrite from '@/views/text2write/textwrite/index.vue'
import FileWrite from '@/views/text2write/filewrite/index.vue'
import WriteToText from '@/views/write2text/index.vue'
const routes = [
  {
    path: '/',
    name: 'layout',
    component: Layout,
    children: [
      {
        path: '',
        name: 'home',
        component: Home
      },
      {
        path: 'write',
        name: 'write',
        component: Write,
        children: [
          {
            path: 'text',
            name: 'fontwrite',
            component: TextWrite
          },
          {
            path: 'file',
            name: 'filewrite',
            component: FileWrite
          }
        ]
      },
      {
        path: 'write2text',
        name: 'WriteToText',
        component: WriteToText,
        meta: {
          title: '手写转文本 - 在线转换工具'
        }
      }
    ]
  },
  {
    path: '/404',
    name: 'notFound',
    component: () => import('../views/404/index.vue'),
    meta: { title: '404' }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: () => import('../views/404/index.vue'),
    meta: { title: '404' }
  }
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
