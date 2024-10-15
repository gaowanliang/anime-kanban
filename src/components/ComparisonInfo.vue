<template>
    <aside class="country__comparison__list-container">
        <div class="country__comparison__title">
            <h3>Comparison with first country</h3>
        </div>
        <ul>
            <li v-for="field in ['confirmed', 'recovered', 'deaths', 'administered']" :key="field"
                class="country__comparison__list__item">
                <span class="country__comparison__list__item__reference">{{ field.charAt(0).toUpperCase() +
                    field.slice(1) }}</span>
                <span class="country__comparison__list__item__value">
                    {{ getComparison(field) }}
                    <img src="../assets/img/information.png" class="calculations-information__info-icon">
                </span>
            </li>
        </ul>
    </aside>
</template>

<script setup>

const props = defineProps(['country', 'referenceCountry'])

const getComparison = (field) => {
    const thisValue = props.country[field] / (field === 'confirmed' ? props.country.population : props.country.confirmed)
    const referenceValue = props.referenceCountry[field] / (field === 'confirmed' ? props.referenceCountry.population : props.referenceCountry.confirmed)
    const comparison = ((thisValue - referenceValue) * 100).toFixed(2)
    return isFinite(comparison) ? (comparison < 0 ? '' : '+') + formatNumber(comparison) + '%' : 'no data'
}

const formatNumber = (number) => new Intl.NumberFormat().format(number)
</script>

<style scoped>
.country__comparison__list-container {
    display: flex;
    flex-direction: column;
    width: 17.5rem;
    filter: drop-shadow(0px 5px 3px rgba(0, 0, 0, 0.4));
    position: relative;
    z-index: 5;
    animation: slideIn 1s;
}

.country__comparison__title {
    width: 100%;
    height: 2rem;
    background-color: var(--color-light-green);
    color: var(--color-white);
    display: flex;
    justify-content: center;
    align-items: center;
}

.country__comparison__list__item {
    display: flex;
    justify-content: space-between;
    width: 100%;
    height: 2rem;
    background-color: var(--color-dark-green);
    color: var(--color-light-green);
    border-bottom: 1px dashed var(--color-light-green);
    padding: 0 1rem;
    align-items: center;
}

.country__comparison__list__item:last-of-type {
    border-bottom: none;
    border-radius: 0 0 5px 5px;
}

.country__comparison__list__item:hover {
    background-color: #1c353f;
}

.calculations-information__info-icon {
    width: 1rem;
    filter: invert(48%) sepia(65%) saturate(410%) hue-rotate(123deg) brightness(95%) contrast(95%);
    margin-left: 0.5rem;
    cursor: help;
}

@keyframes slideIn {
    from {
        transform: translateY(-100%);
    }

    to {
        transform: translateY(0);
    }
}
</style>