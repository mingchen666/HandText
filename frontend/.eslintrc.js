module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true
  },

  extends: [
    'eslint:recommended', // 继承Eslint中推荐的（打钩的）规则项http://eslint.cn/docs/rules/
    'plugin:vue/essential', // 此项是用来配置vue.js风格
    'prettier' // 把prettier中设置的规则添加进来，让它覆盖上面设置的规则。这样就不会和上面的规则冲突了
  ],

  parserOptions: {
    ecmaVersion: 13,
    sourceType: 'module'
  },

  plugins: ['prettier'],
  rules: {
    'prettier/prettier': 'error', //关闭组件命名规则
    'vue/multi-word-component-names': 'off'
  }
}
