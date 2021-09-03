<template>
<div>
  <p>I'm a Counter!</p>
  <p>The current count is:  {{ count }} </p>
  <button v-on:click="count += 1">Add 1</button>
  <button v-on:click="count -= 1">Delete 1</button>
</div>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    };
  }
};
</script>

<style>
</style>

