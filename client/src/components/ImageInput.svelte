<script>
  export let file;
	let  avatar, fileinput;
	
	const onFileSelected = (e) => {
  let image = e.target.files[0];
            let reader = new FileReader();
            reader.readAsDataURL(image);
            reader.onload = e => {
                 avatar = e.target.result
            };
  };
	
</script>
<div class="container">
  <div on:click={() => fileinput.click()} class="avatar">
  {#if avatar}
    <img src={avatar} alt="selected-img" >
  {:else}
    <i class="far fa-images"></i> <span>Select image</span>
  {/if}
  </div>

  <input bind:files={file} style="display: none;" on:change={(e) => onFileSelected(e)} bind:this={fileinput} type="file" accept=".jpg,.png,.jpeg">

</div>

<style>
  .container {
    margin: 1rem;
    text-align: center;
  }
  span {
    display: inline-block;
    font-size: 1rem;
    margin-left: 10px;
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

 