import { useForm } from "react-hook-form";
import { Link, useNavigate } from "react-router-dom"
import axios from 'axios'

import styles from './components.module.css'
import { request_sender, email_regex } from "./functions";


export default function RegForm() {
  const { register, handleSubmit, formState: { errors } } = useForm()
  const navigate = useNavigate()

  const  checkPasswordEquality = (data)  => {
    return data.password == data.rep_password
  } 



  const onSubmit = (data) => {
     
      if(checkPasswordEquality(data)){
        request_sender
        .post("/auth/reg", 
        {
          "email": data.email,
          "username": data.username,
          "password": data.password
        }
      )
       .then( (response) => {
        console.log(response.data)
        navigate("/")
       })
       .catch( (errors) => {
        if (errors.response) {
          alert(errors.response.data.detail)
        }
      })
      }
  }


  return (
    <div className={styles.auth_block} >
      <h3 >Войти</h3>
      <form onSubmit={handleSubmit(onSubmit)} className={styles.login_form}>
        <input {...register(
          "email",
          {
            required: 'Это поле обязательно',
            pattern: {
              value:  email_regex,
              message: "Почта введена неправильно"
            }
          })}
          type="text" placeholder="Введите почту" />
        <p className={styles.error_message}>{errors.email?.message}</p>
        <input {...register("username", { required: 'Это поле обязательно' })} type="text" placeholder="Введите логин" />
        <p className={styles.error_message}>{errors.username?.message}</p>
        <input {...register("password", { required: 'Это поле обязательно' })} type="password" placeholder="Введите пароль" />
        <p className={styles.error_message}>{errors.password?.message}</p>
        <input {...register("rep_password", { required: 'Это поле обязательно' })} type="password" placeholder="Повторите пароль" />
        <p className={styles.error_message}>{errors.rep_password?.message}</p>
        <button type="submit" >Отправить</button>
      </form>
      <Link to='/login'>У вас уже есть аккаунт?</Link>
    </div>
  );
}