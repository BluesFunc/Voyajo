import axios from "axios"
import { redirect, useLocation } from "react-router-dom"

export const email_regex = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/


export const request_sender = axios.create({
    baseURL : " http://127.0.0.1:8000",
    timeout: 1000
}
)

export default function logout(){
    const location = useLocation
    localStorage.removeItem("UserToken")
    location('/')
}
