<script>
  import { fade, fly } from 'svelte/transition';
  export let txt = "Place holder message";
</script>

<div in:fly="{{ y: 200, duration: 1000 }}" out:fade>
  <span>{txt}</span>
</div>

<style>
  div {
    font-size: 1rem;
    margin: 2rem auto;
    text-align: center;
    background-color: var(--dark-color);
    color:rgb(255, 255, 255);
    width: 275px;
    height: 40px;
    border: 2px solid white;
    border-radius: 15px;
    font-weight: bold;
    display: flex;

    align-items: center;
    justify-content: center;
  }
 
</style>