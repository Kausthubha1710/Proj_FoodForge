axios.get(`https://api.spoonacular.com/recipes/findByIngredients?apiKey=${spoonacularAPIKEY}`).then((response) => {
    console.log(response.data);
});

