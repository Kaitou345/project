<script>
  import Navbar from "./components/Navbar.svelte";
  import TextInput from "./components/TextInput.svelte";
  import SubmitButton from "./components/SubmitButton.svelte";
  import Heading from "./components/Heading.svelte";
  import CheckData from "./components/CheckData.svelte";
  import Form from "./components/Form.svelte"; 
  import {selectedSection} from "./stores"
</script>
<Navbar />
{#if $selectedSection===1}
  <CheckData />
{:else if $selectedSection===2}
  <Form />
{/if}
