<script>
  export let title;
</script>

<button on:click>{title}</button>

<style>
  button {
    margin: 1rem;
    height: var(--field-height);
    width: var(--field-width);
    background-color: var(--highlight-color);
    border-radius: 6px;
    border: none;
    font-size: 1rem;
  }
  button:hover {
    background-color: var(--focus-color);
    cursor: pointer;
  }
</style>