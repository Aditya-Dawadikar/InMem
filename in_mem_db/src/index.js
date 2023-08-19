import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


import Home from './app/screens/Home';
import Workbench from './app/screens/Workbench';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home/>,
  },{
    path: "/workbench/:db_name",
    element: <Workbench/>,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router}>
    <App />
    </RouterProvider>
  </React.StrictMode>
);
