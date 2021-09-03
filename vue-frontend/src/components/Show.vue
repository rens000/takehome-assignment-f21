<template>
  <div>
    <b>{{name}}:</b>  
    <Counter :episodes_seen=this.episodes_seen />
    <br/>
  </div>

</template>

<script>

import Counter from "./Counter.vue";
// PART 4: Add your code here
export default {
  components: {
    Counter
  },
  props: {
    name: {
      type: String,
    },
    id: {
      type: Number,
    },
    episodes_seen: {
      type: Number,
    }
  }
};
</script>

<style>
</style>
