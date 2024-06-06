import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';

import { createBrowserRouter, RouterProvider } from "react-router-dom"



import BasePage from './pages/BasePage'
import LoginPage from './pages/LoginPage';
import RegPage from './pages/RegPage';
import AdminPage from './pages/AdminPage';


import './index.css'
import CustomerPage from './pages/CustomerPage';
import ExtranetPage from './pages/ExtranetPage';
import Company_block from './components/company_block';
import { companies_loader } from './utils/loaders';
import { CompanyForm } from './components/extranet_forms';

const router = createBrowserRouter([
  {
    path: "/",
    element: <BasePage />,
    children: [
      {
        path: "login/",
        element: <LoginPage />
      },
      {
        path: "reg/",
        element: <RegPage />
      }
    ],
  },
  {
    path: '/admin',
    element: <AdminPage />
  },
  {
    path: '/customer',
    element: <CustomerPage />,
    children: [
      {
        path: ':id',
      }
    ]
  },
  {
    path: '/extranet',
    element: <ExtranetPage />,
    children: [
      {
        path: ':id',
        element: <Company_block />,
        loader: companies_loader
      },
      {
        path: ':id/company/add',
        element: <CompanyForm />,
      },
     

    ]
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
