<script>
  export let placeholder = "Enter name here...";
  export let text;
</script>

<input bind:value={text} type="text" {placeholder}>

<style>
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