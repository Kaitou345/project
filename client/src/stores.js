import {writable} from 'svelte/store';

export const sections = [
  {
    text: "Check",
    id: 1
  },
  {
    text: "Register",
    id: 2
  },
  {
    text: "Delete",
    id: 3
  }
];

export const selectedSection = writable(sections[0].id)