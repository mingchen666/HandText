import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useFormDataStore = defineStore(
  'form-data',
  () => {
    // 默认所有表单值
    const defaultForm = {
      baseForm: {
        fill: 'rgb(0, 0, 0)', // 字体颜色
        text: '',
        width: 2479,
        height: 3508,
        isUnderlined: false,
        font_option: '云烟体.ttf',
        font_size: 80,
        background_image: null,
        pdf_save: false
      },
      marginForm: {
        line_spacing: 90,
        word_spacing: 1,
        top_margin: 20,
        bottom_margin: 20,
        left_margin: 20,
        right_margin: 20
      },
      advancedForm: {
        line_spacing_sigma: 1.0, // 行间距的随机扰动值
        font_size_sigma: 2.0, // 字体大小的随机扰动值
        word_spacing_sigma: 2.0, // 单词间距的随机扰动值
        perturb_x_sigma: 3.0, // 笔画横向偏移的随机扰动值
        perturb_y_sigma: 3.0, // 笔画纵向偏移的随机扰动值
        perturb_theta_sigma: 0.05, // 笔画旋转偏移的随机扰动值
        strikethrough_probability: 0.05, // 删除线的概率
        strikethrough_length_sigma: 2.0, // 删除线长度的随机扰动值
        strikethrough_width_sigma: 2.0, // 删除线宽度的随机扰动值
        strikethrough_angle_sigma: 2.0, // 删除线角度的随机扰动值
        strikethrough_width: 8.0, // 删除线的宽度
        ink_depth_sigma: 30.0 // 墨水深度的随机扰动值
      }
    }
    const baseForm = ref({ ...defaultForm.baseForm })
    const marginForm = ref({ ...defaultForm.marginForm })
    const advancedForm = ref({ ...defaultForm.advancedForm })

    const updateBaseForm = (newForm) => {
      baseForm.value = newForm
    }

    const updateMarginForm = (newForm) => {
      marginForm.value = newForm
    }
    const updateAdvancedForm = (newForm) => {
      advancedForm.value = newForm
    }
    // const doubleCount = computed(() => count.value * 2)
    // 重置表单
    const resetAllForm = () => {
      baseForm.value = { ...defaultForm.baseForm }
      marginForm.value = { ...defaultForm.marginForm }
      advancedForm.value = { ...defaultForm.advancedForm }
    }

    return {
      baseForm,
      marginForm,
      advancedForm,
      updateBaseForm,
      updateMarginForm,
      updateAdvancedForm,
      resetAllForm
    }
  },
  {
    persist: true //持久化存储
  }
)
