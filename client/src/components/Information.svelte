<script>
  import ImageInput from "./ImageInput.svelte";
  import SubmitButton from "./SubmitButton.svelte";
  import TextInput from "./TextInput.svelte";
  import TextInputLg from "./TextInputLg.svelte";
  import Heading from "./Heading.svelte";

  export let name;
  export let age;
  export let email;
  export let address;
  export let contact_number;

  export let img1 = null;

  async function onSubmit()
  {

  }

</script>
<div>
  <Heading adjust={true} title="Information" />
  <div class="container">
    <div class="sub-container-1">
      <div class="flex">
        <ImageInput bind:file={img1} />
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


