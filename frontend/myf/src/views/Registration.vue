<template>
    <div>
        <b-form @submit="onSubmit">
            <b-form-group
                id="input-group-1"
                label="Username:"
                label-for="input-1"
              >
                <b-form-input
                  id="input-1"
                  v-model="new_user.username"
                  required
                  placeholder="Enter username"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="input-group-2"
                label="Name:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="new_user.first_name"
                  required
                  placeholder="Enter Your Name"
                ></b-form-input>
            </b-form-group>

            <b-form-group 
                id="input-group-3" 
                label="LastName:" 
                label-for="input-3"
                >
                <b-form-input
                  id="input-3"
                  v-model="new_user.last_name"
                  required
                  placeholder="Enter Your LastName"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-4" label="Email:" label-for="input-3">
                <b-form-input
                  id="input-4"
                  v-model="new_user.email"
                  required
                  placeholder="Enter Email"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-4" label="Password:" label-for="input-3">
                <b-form-input
                  id="input-4"
                  v-model="new_user.password"
                  required
                  placeholder="Enter Password"
                ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </div>
</template>

<script>
    import {config} from "../../config";

    export default {
        name: "Registration",
        data() {
            return {
                new_user: {
                    username: '',
                    first_name: '',
                    last_name: '',
                    email: '',
                    password: '',
                }
            }
        },

        methods: {
            onSubmit: function (e) {
                e.preventDefault();
                fetch(config.api_path + 'user/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                  },
                  body: JSON.stringify(this.new_user)
                }).then(() => {
                    this.$router.push('/');
                });
            }
        }
    }
</script>