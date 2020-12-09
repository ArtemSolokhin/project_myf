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

            <b-form-group id="input-group-4" label="Password:" label-for="input-3">
                <b-form-input
                  id="input-4"
                  v-model="new_user.password"
                  required
                  placeholder="Enter Password"
                ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">SignIn</b-button>
        </b-form>
    </div>
</template>

<script>
    import {config} from "../../config";

    export default {
        name: "SignIn",
        data() {
            return {
                new_user: {
                    username: '',
                    password: '',
                }
            }
        },

        methods: {
            onSubmit: function (e) {
                e.preventDefault();
                fetch(config.api_path + 'user/', {
                  method: 'GET',
                  headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                  },
                  body: JSON.stringify(this.new_user)
                }).then(() => {
                    this.$router.push('/profile');
                });
            }
        }
    }
</script>