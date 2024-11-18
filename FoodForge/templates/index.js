axios.get(`https://api.spoonacular.com/recipes/complexSearch?apiKey=${spoonacularAPIKEY}`).then((response) => {
    console.log(response.data);
});

