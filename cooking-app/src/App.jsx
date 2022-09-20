import { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";

import Homepage from "./views/homepage/Homepage";
import RecipesList from "./views/recipes list/RecipesList";

export default function App() {
  return (
    <Routes>
    <Route exact path="/" element={<Homepage />} />
      <Route path="/recipes-list" element={<RecipesList />} />
    </Routes>
  );
}
