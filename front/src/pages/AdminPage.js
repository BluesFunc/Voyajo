import Admin from "react-crud-admin"
import { request_sender } from "../components/functions";


export default class AdminPage extends Admin {
    constructor(){
        super();
        this.name = 'User';
        this.name_plural = 'Users';
        this.list_display_links = ['1'];
        this.list_display = ["id", "email", "username", 'hashed_password']
    }
    get_queryset(page_number, list_per_page, queryset) {
        const response_data = request_sender
        .get('/admin/user')
        .then( (response) => {
            console.log(response)
            this.set_queryset(response.data)
        })
        return queryset
      }

}