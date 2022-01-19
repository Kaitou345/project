<script>
  export let placeholder = "Enter name here...";
  export let text;
  export let label;
  export let editable = true;
</script>
{#if !editable}
<div class="container">
  <label>{label}</label>
  <input readonly bind:value={text} type="text" {placeholder}>
</div>
{:else}
<input bind:value={text} type="text" {placeholder}>
  
{/if}
<style>
    label {
    font-size: 1rem;
    margin-right: 2.5rem;
  }
  .container {
    margin:1rem;
    display: inline-flex;
    place-content: left;
    min-width: 600px;
    align-items: center;
  }
  input {
    width: calc(var(--field-width) * 2 + 45px) ;
    height: var(--field-height);
    background-color: var(--dark-color);
    border: 1px solid white;
    border-radius: 5px;
    box-sizing: border-box;
    padding: 1rem;
    margin: 1rem;
    color: white;
  }

  input::placeholder {
    color: #fff
  }

  input:focus {
    outline: none;
  }
  
</style>