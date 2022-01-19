<script>
  export let data;
</script>
<div class="container">
  <div class="avatar">
    <img src='data:image/jpeg;base64, {data}' alt="Profile" >
  </div>

</div>

<style>
  .container {
    margin: 1rem;
    text-align: center;
  }
  .avatar {
    background-color: var(--dark-color);
    display: inline-block;
    width: 200px;
    height: 200px;
    border: 3px white solid;
    border-radius: 10px;
    display: flex;
    align-items: center;
    place-content: center;

    cursor: pointer;
  }

  img {
    display: inline-flex;
    height: 200px;
    width: 200px;
    border-radius: 10px;
  }
</style>

 