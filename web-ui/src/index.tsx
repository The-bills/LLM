import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  BrowserRouter,
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import "./index.css";
import { Home } from "./views/Home/Home";
import { CvList } from "./views/CvList/CvList";
import { Cv } from "./views/Cv/Cv";
import { QueryClient, QueryClientProvider } from "react-query";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/cv",
    element: <CvList />,
  },
  {
    path: "/cv/:cvId",
    element: <Cv />,
  },
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <QueryClientProvider client={new QueryClient()}>
          <RouterProvider router={router} />
    </QueryClientProvider>
  </React.StrictMode>
);
