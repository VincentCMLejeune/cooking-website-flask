import { useState, useEffect } from "react";

export default function RecipesList() {
  const [recipesList, setRecipesList] = useState();

  useEffect(() => {
    fetch("/recipes-list")
      .then((res) => res.json())
      .then((data) => {
        setRecipesList(data.recipes);
      });
  }, []);

  return (
    <div>
      <h1>Recipes list</h1>
      {recipesList && recipesList.map((recipe) => <p>{recipe}</p>)}
    </div>
  );
}
