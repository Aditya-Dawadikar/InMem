import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Provider } from 'react-redux';
import store from './app/redux/store';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


import Home from './app/screens/Home';
import Workbench from './app/screens/Workbench';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  }, {
    path: "/workbench/:db_name",
    element: <Workbench />,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <RouterProvider router={router}>
        <App />
      </RouterProvider>
    </Provider>
  </React.StrictMode>
);
