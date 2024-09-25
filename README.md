
![обложка1](https://github.com/user-attachments/assets/93c8e315-d91e-4076-980b-6bba40b66471)

 
| Участник | Роль | Задача |
|----------|------|--------|
| Шерстобитов Олег Андреевич | Программист | Программирование дрона |
| Ржанникова Елена Андреевна | Программист | Работа с ИИ |

## Проблема и цель
По статистике ГИБДД в 2023 году 33% ДТП произошло из-за некачественных дорог. То есть, каждый 3 водитель рискует повредить машину из-за ямы или выбоены. Основной причиной плохого состояния дорожного полотна является несвоевременное обнаружение и ремонт повреждений. Мы предлогаем при помощи автономного дрона выполнять облет дорог, при помощи нейросети обнаруживать ямы и передавать информацию в дорожные службы. А при помощи автономного ровера выполнять ремонт этих ям.
## Описание работы
Квадрокоптер автономно выполняет облет городских улиц и при помощи нейронной сети обнаруживает ямы и дефекты дорожного полотна. Все данные о найденных дефектах отправляются на сервер, который составляет карту повреждений. По ночам, когда автомобилей на дорогах меньше, автономный ровер выезжает на ремонт дороги. Он передвигается по заранее составленному маршруту, соблюдая ПДД, распознавая показания светофоров и прочее. По прибытии на место работ ровер при помощи лидара сканирует яму, определяет ее размер и объем. На основе полученных данных он принимает решение о самостоятельном ремонте либо же передаче информации о том, что эту яму необходимо устранять вручную. Если яма пригодна для автономного ремонта, он подает необходимый объем асфальтобетонной смеси в яму, а затем проезжается по ней, выравнивая ее.
## Требования к системе:
- Квадрокоптер должен быть способен автономно выполнять облет городских улиц.
- Нейросеть должна обрабатывать изображение с камеры дрона и распозновать разные ямы.
- Сервер должен составлять карту повреждений на основе данных, полученных от квадрокоптера.
- Автономный ровер должен передвигаться по заранее составленному маршруту, соблюдать ПДД и распознавать показания светофоров.
- Ровер должен иметь систему сканирования ям при помощи лидара.
- Система должна принимать решение о самостоятельном ремонте либо же передаче информации о том, что эту яму необходимо устранять вручную.
## Задачи проекта
- Подготовить датасет и обучить нейронную сеть на распознавание ям тестовой карты.
- Настроить дрон под работу в автономном режиме. Загрузить и отладить работу нейронной сети на дроне.
- Разработать алгоритм работы с результатами распознавания: подсчет количества ям, определение их координат, передача данных на сервер.
- Разработать серверное приложение с функцией приема данных с дрона, обработке данных о ямах, сборе статистики и передаче информации об обнаруженных ямах пользователям.
- Протестировать систему и внести изменения на основе результатов тестирования.

  
[**`Задачи`**](https://github.com/user-attachments/files/17129173/Tasks.xlsx)


[**`Реализация проекта`**](https://github.com/ElenaRzh/Autonomous-road-surface-monitoring-and-repair-system./blob/main/DEVELOPMENT.md)



