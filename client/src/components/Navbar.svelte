<script>
  import NavItems from "./NavItems.svelte"; 
</script>

<div class="navbar">
  <div class="container">
      <NavItems />
  </div>  
</div>

<style>
  .navbar {
    margin: 1rem 2rem ;
    position: sticky;
  }

  .container {
    padding-left: 10rem;
    padding-right: 10rem;

    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>