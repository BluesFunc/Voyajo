import { useForm } from "react-hook-form";
import { request_sender } from "./functions";
import { useNavigate } from "react-router-dom";

import styles from './components.module.css'


export function CompanyForm() {

    const { register, handleSubmit, formState: { errors } } = useForm();
    const extranet_id = localStorage.getItem('RoleID')
    const navigate = useNavigate()

    const onClick = (data) => {
        request_sender
            .post(
                ('distributing/extranet/' +  extranet_id  + '/company'),
                data
            )
            .catch((errors) => {
                console.log(errors)
                console.log(data)
                return errors
            })
            .then(
                alert("Компания успешно создана")
            )
    }

    return (
        <div className={styles.auth_block} >
            <h3 >Компания</h3>
            <form onSubmit={handleSubmit(onClick)}className={styles.login_form}>


                <input {...register("name", { required: 'Это поле обязательно' })} type="text" placeholder="Название компании" />
                <p className={styles.error_message}>{errors.name?.message}</p>
                <input {...register("company_link", { required: 'Это поле обязательно' })} type="text" placeholder="Ссылку на компанию" />
                <p className={styles.error_message}>{errors.company_link?.message}</p>

                <select {...register("company_type", { required: "Это поле обязательно" })}>
                    <option value="Airline">Авиа</option>
                    <option value="Bus">Автобусная</option>
                    <option value="Railway">Железнодорожная</option>
                </select>
                <p className={styles.error_message}>{errors.rep_password?.message}</p>
                <button type="submit" >Отправить</button>
            </form>

        </div>
    )

}

