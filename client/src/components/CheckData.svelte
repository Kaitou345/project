<script>
import Heading from "./Heading.svelte";
import ImageInput from './ImageInput.svelte';
import SubmitButton from './SubmitButton.svelte';
import Message from "./Message.svelte";
import Information from "./Information.svelte";
import {api} from "../stores";


let title = "Check Data";
let file = null;

let foundData = null;


let found = false;
let entered = false;
let loading = false;

async function onSubmit() {
  loading = true;
  const data = new FormData();
  if(!file)
  {
    loading = false;
    return;
  }
  data.append("img_to_check", file[0]);

  const response = await fetch(api + "/check", {
      method: 'POST',
      body: data
  });
  
  if(response.ok)
  {
    const json = await response.json();
    foundData = json.data;
    found = true;
    console.log(foundData);
  }
  else
  {
    console.log("ERRORR!!");
  }
  loading = false;
}

</script>

<div class="container">
  <Heading {title} />
  <div class="flex">
    <ImageInput bind:file={file} />
    <SubmitButton on:click={onSubmit} title="Check" />
  </div>
  
  {#if loading}
    <Message txt="Checking the image!" />    
  {:else if entered && !found}
    <Message txt="There was no match!" />    
  {:else if found}
    <Information data={foundData}/>
  {/if}

</div>

<style>
  .container{
    text-align: center;
  }

  .flex {
    display: flex;
    flex-direction: column;
    place-content: space-between;
    align-items: center;

  }
</style>
