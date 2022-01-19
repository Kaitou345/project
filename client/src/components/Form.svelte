<script>
  import SubmitButton from "./SubmitButton.svelte";
  import TextInput from "./TextInput.svelte";
  import ImageInput from "./ImageInput.svelte";
  import Heading from "./Heading.svelte";
  import TextInputLg from "./TextInputLg.svelte";
  import Message from './Message.svelte';


  export let name;
  export let age;
  export let email;
  export let address;
  export let contact_number;

  export let img1 = null;
  export let img2 = null;

  let success = false;
  let loading = false;

  async function onSubmit()
  {
    loading = true;
    const data = new FormData();
    data.append("name", name);
    data.append("age", age);
    data.append("email", email);
    data.append("address", address);
    data.append("contact_number", contact_number);
    
    if  (!(img1 && img2))
    {
      loading = false;
      return;
    }
    data.append("img1", img1[0]);
    data.append("img2", img2[0]);


    const response = await fetch("http://192.168.1.4:3000/register", {
      method: 'POST',
      body: data
    });

    if(response.ok)
    {
      success = true;
      setTimeout(() => success = false, 3000);
    }
    loading = false;
    
  }

  const revaluate = () => { 
    if (loading)
    {
      return "Registration in progress!";
    }
    else if (success)
    {
      return "Registration successful!";
  }}; 

  $: messageText = loading ? "Registration in progress!" : success ? "Registration successful!" : "Debug Text";
  

</script>
<div>
  <Heading adjust={true} title="Register" />
  <div class="container">
    <div class="sub-container-1">
      <div class="flex">
        <ImageInput bind:file={img1} />
        <ImageInput bind:file={img2} />
      </div>
    </div>
  
    <div class="sub-container-2">
      <TextInput bind:text={name}  placeholder={"Name"} />
      <TextInput bind:text={email}  placeholder={"Email"} />
      <TextInput bind:text={age}  placeholder={"Age"} />
      <TextInput bind:text={contact_number} placeholder={"Contact Number"} />
      <TextInputLg bind:text={address}  placeholder={"Address"} />
  
      <SubmitButton on:click={onSubmit}/>
    </div>
  </div>

  {#if success} 
    <Message txt={messageText} />
  {:else if loading}
    <Message txt={messageText}/>
  {/if}
    
</div>


<style>

  .container {
    display: flex;
    place-content: space-between;

  }
  .sub-container-1 {
    place-content: center;
    border-right: 3px solid var(--focus-color);
  }
  .sub-container-2 {
    margin-left: 2rem;    
  }
  .flex {
    display: flex;
    margin-right: 2rem;
    margin-left: 2rem;

  }
</style>


