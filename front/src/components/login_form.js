import { useForm } from "react-hook-form";
import { Link, useNavigate } from "react-router-dom";

import styles from './components.module.css'
import { request_sender, email_regex } from "./functions";

export default function LoginForm() {
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate()
  const onSubmit = (data) => {
    request_sender
      .post("/auth/send",
        data
      )
      .then((response) => {

        localStorage.setItem("User", response.data.username)
        localStorage.setItem("UserRole",response.data.user_role)
        localStorage.setItem("RoleID",response.data.role_id)
        navigate('/')
        window.location.reload()
        console.log(response.data)
      })
      .catch((error) => { alert(error.response.data.detail) })

}
return (
  <div className={styles.auth_block} >
    <h3 style={{ "text-align": "center" }}>Войти</h3>
    <form onSubmit={handleSubmit(onSubmit)} className={styles.login_form}>
      <input {...register("email",
        {
          required: true,
          pattern: {
            value: email_regex,
            message: "Почта введена неверно"
          }
        })} type="text" placeholder="Введите почту" />
      <input {...register("password", { required: true })} type="password" placeholder="Введите пароль" />
      <button type="submit" >Отправить</button>
    </form>
    <Link to='/reg'>У вас еще нет аккаунта? </Link>
  </div>
);
}
