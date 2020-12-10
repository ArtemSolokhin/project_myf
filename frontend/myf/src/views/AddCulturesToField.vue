<template>
    <div>
        <b-form @submit="onSubmit">
            <b-form-group id="input-group-1" label="culture:" label-for="input-1">
                <b-form-select
                  id="input-1"
                  v-model="new_culture.culture"
                  :options="cultures"
                  required
                ></b-form-select>
            </b-form-group>

            <b-form-group
                id="input-group-2"
                label="harvest date:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="new_culture.harvest_date"
                  type="date"
                  required
                  placeholder="Enter harvest date"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-3" label="field:" label-for="input-3">
                <b-form-select
                  id="input-3"
                  v-model="new_culture.field"
                  :options="fields"
                  required
                ></b-form-select>
            </b-form-group>

            <b-form-group
                id="input-group-4"
                label="Length:"
                label-for="input-4"
              >
                <b-form-input
                  id="input-4"
                  v-model="new_culture.length"
                  type="number"
                  required
                  placeholder="Enter length"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="input-group-5"
                label="Width:"
                label-for="input-5"
              >
                <b-form-input
                  id="input-5"
                  v-model="new_culture.width"
                  type="number"
                  required
                  placeholder="Enter width"
                ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Create</b-button>
        </b-form>
    </div>
</template>

<script>
    import {config} from "../../config";
    export default {
        name: "AddCulturesToField",
        data() {
            return {
                new_culture: {
                    culture: '',
                    length: '',
                    width: '',
                    harvest_date: '',
                    field: '',
                },
                fields: [{
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
            let response = await fetch(config.api_path + 'field/');
            response = await response.json();
            
            for(let key in response) {
                
                this.fields.push({
                    value: response[key].id,
                    text: response[key].id
                })
            }
            
            let responce = await fetch(config.api_path + 'culture/');
            responce = await responce.json();
            for(let key in responce) {
                console.log(responce[key].name)
                this.cultures.push({
                    value: responce[key].id,
                    text: responce[key].name
                })
            }
            
        },
        
        methods: {
            onSubmit: function (e) {
                e.preventDefault();
                fetch(config.api_path + 'dates-cults/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                  },
                  body: JSON.stringify(this.new_culture)
                }).then(() => {
                    this.$router.push('/');
                });
            }
        }
    }
</script>