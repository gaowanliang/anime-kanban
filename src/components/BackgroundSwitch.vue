<template>
    <div class="switch-background-btn-container" @click="toggle">
        {{ isOn ? 'ON' : 'OFF' }}
        <div :class="['switch-background-btn', { 'flip-switch-on': isOn }]"></div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const isOn = ref(true)

const toggle = () => {
    isOn.value = !isOn.value
    emit('toggle')
}

const emit = defineEmits(['toggle'])
</script>

<style scoped>
.switch-background-btn-container {
    position: fixed;
    top: 0;
    right: 10%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    cursor: pointer;
    width: 1.875rem;
    height: 3.125rem;
    background-color: var(--color-white);
    border-radius: 0 0 20px 20px;
    box-shadow: var(--shadow-white-transparent);
    color: var(--color-light-green);
    font-size: 0.7rem;
}

.switch-background-btn {
    width: 1.25rem;
    height: 1.25rem;
    background-color: var(--color-light-green);
    border-radius: 50%;
    transition: all 0.2s;
}

.switch-background-btn:hover {
    background-color: var(--color-dark-green);
}

.flip-switch-on {
    transform: translateY(-0.625rem);
}
</style>