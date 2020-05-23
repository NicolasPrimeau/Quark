<script>
	export let registerURL;
	export let apiURL;
	let request;
	let requestError = null;

	function validateRequest(url) {
		// Add more later
		requestError = null;

		if (!/\.[a-z]{2,9}$/i.test(url)) {
			requestError = new Error('Invalid URL')
			return null;
		}

		if (!/^https?/.test(url)) {
			return `http://${url}`;
		}

		return url;
	}

	function handleSubmit(e) {
		e.preventDefault()
		const url = validateRequest(e.target[0].value)

		if (url === null) return;

		request = registerURL(url)
				.catch(e => requestError = e.message);
	}
</script>

<main>
<h1>Hello friend!</h1>
{#if !!request || request === null}
	{#await request}
		<p>wait for it...</p>
  {:then value}
		<p>Your🤏new🤏link🤏is: <a href="{`${apiURL}l/${value.data.alias}`}">{`${apiURL}l/${value.data.alias}`}</a> 🤏</p>
  {:catch error}
		<p>Something went wrong: {error.message}</p>
  {/await}

{:else if requestError}
	<p>{requestError}</p>

{:else}
	<p>give me a link to shorten!!!</p>
{/if}

<form on:submit={handleSubmit}>
	<input value="" type="text">
	<button type="submit">fart! ☁☁</button>
</form>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
