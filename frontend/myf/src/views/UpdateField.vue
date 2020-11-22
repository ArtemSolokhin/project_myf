<template>
    <div>
        <b-form @submit="onSubmit">
            <b-form-group
                id="input-group-1"
                label="Length:"
                label-for="input-1"
              >
                <b-form-input
                  id="input-1"
                  v-model="new_field.length"
                  type="number"
                  required
                  placeholder="Enter length"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="input-group-2"
                label="Width:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="new_field.width"
                  type="number"
                  required
                  placeholder="Enter width"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-3" label="Owner:" label-for="input-3">
                <b-form-select
                  id="input-3"
                  v-model="new_field.owner"
                  :options="users"
                  required
                ></b-form-select>
            </b-form-group>

            <b-form-group id="input-group-4" label="Cultures:" label-for="input-3">
                <b-form-select
                  id="input-4"
                  v-model="new_field.cultures"
                  :options="cultures"
                  required
                ></b-form-select>
            </b-form-group>

            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </div>
</template>

<script>
    import {config} from "../../config";

    export default {
        name: "UpdateField",
        data() {
            return {
                new_field: {
                    length: '',
                    width: '',
                    owner: '',
                    cultures: '',
                },
                users: [{
                    value: null,
                    text: 'Select One'
                }],
                cultures: [{
                    value: null,
                    text: 'Select One'
                }]
            }
        },
        async mounted() {
            let response = await fetch(config.api_path + 'user/');
            response = await response.json();

            for(let key in response) {
                this.users.push({
                    value: response[key].id,
                    text: response[key].username
                })
            }

            response = await fetch(config.api_path + 'dates-cults/');
            response = await response.json();
            for(let key in response) {
                this.cultures.push({
                    value: response[key].id,
                    text: response[key].culture.name
                })
            }
        },
        methods: {
            onSubmit: function (e) {
                e.preventDefault();
                fetch(config.api_path + 'field/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                  },
                  body: JSON.stringify(this.new_field)
                }).then(() => {
                    this.$router.push('/');
                });
            }
        }
    }
</script>