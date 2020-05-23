import App from './App.svelte';
import { apiURL, registerURL } from './api';

const app = new App({
	target: document.body,
	props: {
		apiURL,
		registerURL,
	}
});

export default app;
