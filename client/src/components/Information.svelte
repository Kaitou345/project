<script>
  import ImageB64 from "./ImageB64.svelte";
  import SubmitButton from "./SubmitButton.svelte";
  import TextInput from "./TextInput.svelte";
  import TextInputLg from "./TextInputLg.svelte";
  import Heading from "./Heading.svelte";
  import {api} from "../stores";
  import Message from './Message.svelte';
import { slide } from "svelte/transition";
import { text } from "svelte/internal";

  export let data;


  let loading = false;
  let done = false;
  let failed = false;
  async function onSubmit()
  {
    loading = true;
    const form = new FormData();

    form.append("id", data.id)
    
    const response = await fetch(api + "/delete", {
      method: "POST",
      body: form
    });
    
    done = true;
    failed = true;
    if(response.ok)
    {
      loading = false;
      failed = false;
      
    }
    setTimeout(() => {done = false}, 3000);
    
  }

</script>
<div class="info">
  <Heading adjust={true} title="Information" />
  <div class="container">
    <div class="sub-container-1">
      <div class="flex">
        <ImageB64 data={data.image} />
      </div>
    </div>
  
    <div class="sub-container-2">
      <TextInput label={"Name"} editable={false} bind:text={data.name}  placeholder={"Name"} />
      <TextInput label={"Email"} editable={false} bind:text={data.email}  placeholder={"Email"} />
      <TextInput label={"Age"} editable={false} bind:text={data.age}  placeholder={"Age"} />
      <TextInput label={"Number"} editable={false} bind:text={data.contact_number} placeholder={"Contact Number"} />
      <TextInputLg label={"Address"} editable={false} bind:text={data.address}  placeholder={"Address"} />
  
      <SubmitButton title="Delete" on:click={onSubmit}/>

      {#if loading}
        <Message txt = "Deleting information" />
      {:else if (done && failed) }
        <Message txt = "Failed to delete" />
      {:else if (done && !failed) }
        <Message txt = "Deleted Successfully" />
      {/if}
    </div>
  </div>
</div>


<style>

  .container {
    display: inline-flex;
    place-content: space-between;

  }
  .sub-container-1 {
    place-content: center;
    border-right: 3px solid var(--focus-color);
  }
  .sub-container-2 {
    margin-left: 2rem;
    text-align: left;
  }
  .flex {
    display: flex;
    margin-right: 2rem;
    margin-left: 2rem;

  }
  .info {
    margin: 5rem auto;
    height: 90vh;
  }
</style>


