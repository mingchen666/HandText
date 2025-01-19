<template>
  <div class="text-input-section">
    <div class="custom-alert">
      <i class="alert-icon"></i>
      <div class="alert-content">
        <h4 class="alert-title">{{ $t('write2text.alert.title') }}</h4>
        <div class="alert-description">
          <p>1.{{ $t('write2text.alert.description.1') }}</p>
          <p>2.{{ $t('write2text.alert.description.2') }}</p>
          <p>3.{{ $t('write2text.alert.description.3') }}</p>
          <p>4.{{ $t('write2text.alert.description.4') }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
<style scoped>
.text-input-section {
  margin-top: 50px;
}
.custom-alert {
  display: flex;
  align-items: flex-start;
  background-color: #f9e5ca;
  border-radius: 4px;
  border-left: 5px solid #f19a18;
  padding: 15px 10px;
  margin-bottom: 15px;
}
.alert-icon {
  width: 24px;
  height: 24px;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-exclamation-octagon" viewBox="0 0 16 16"><path d="M4.54.146A.5.5 0 0 1 4.893 0h6.214a.5.5 0 0 1 .353.146l4.394 4.394a.5.5 0 0 1 .146.353v6.214a.5.5 0 0 1-.146.353l-4.394 4.394a.5.5 0 0 1-.353.146H4.893a.5.5 0 0 1-.353-.146L.146 11.46A.5.5 0 0 1 0 11.107V4.893a.5.5 0 0 1 .146-.353L4.54.146zM5.1 1 1 5.1v5.8L5.1 15h5.8l4.1-4.1V5.1L10.9 1H5.1z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>');
  background-size: cover;
  margin-right: 10px;
}
.alert-content {
  flex: 1;
}
.alert-title {
  font-size: 18px;
  /* margin-left: 10px; */
  font-weight: bold;
  margin-bottom: 5px;
  color: #e6a23c;
}
.alert-description {
  font-size: 14px;
  color: #999;
}
.alert-description p {
  margin: 8px auto;
}
</style>
