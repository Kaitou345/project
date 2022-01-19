<script>
  import {sections, selectedSection} from '../stores.js'

  function onSelect(id) {
    selectedSection.update(value => {
      return id;
    })
  }

</script>
<nav>
  <ul>
    {#each sections as section (section.id)}
      <button on:click={() => onSelect(section.id)}>{section.text}</button>
    {/each}
  </ul>
</nav>

<style>
    ul {
    display: flex;
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  button {
    margin: 1rem;
    border: none;
    background: none;
    color: var(--highlight-color);
    font-size: 1.1rem;
  }
  button:hover {
    color: var(--focus-color);
    cursor: pointer;
  }
</style>