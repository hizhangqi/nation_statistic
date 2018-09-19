<template>

  <div class="block">
    <span class="demonstration">省份/城市/地区</span>
    <el-cascader
      :options="options"
      v-model="selectedOptions"
      :separator="'/'"
      :props="props"
    >
    </el-cascader>
  </div>
 </template>

<script>
  import provincecity from '@/const/province_city'
export default {
data() {
  return {
    options:	provincecity,
    selectedOptions:"",
    props:{
      value:'PROVINCE_ID',
      label:'PROVINCE_NAME',
      children:"CITIES"
    }

  }
},
  methods:{
    getInit(){
      console.log(this.options);
    }
  },
  mounted(){
    this.getInit();
  }
};
</script>
