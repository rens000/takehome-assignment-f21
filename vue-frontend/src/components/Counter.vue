<template>
<div>
  <p>{{ count }} episodes seen</p>
  <button v-on:click="count += 1">Add 1</button>
  <button v-on:click="count -= 1">Delete 1</button>
</div>
</template>

<script>
export default {
  props: {
    episodes_seen: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      count: this.episodes_seen
    };
  }
};
</script>

<style>
</style>

