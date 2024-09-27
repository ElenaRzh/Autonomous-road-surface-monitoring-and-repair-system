
![обложка](https://github.com/user-attachments/assets/bcc1f9ae-6509-4df7-81dd-e649f194b141)


 
| Участник | Роль | Задача |
|----------|------|--------|
| Шерстобитов Олег Андреевич | Программист | Программирование дрона |
| Ржанникова Елена Андреевна | Программист | Работа с ИИ |

## Проблема и цель
По статистике ГИБДД в 2023 году 33% ДТП произошло из-за некачественных дорог. То есть, каждый 3 водитель рискует повредить машину из-за ямы или выбоины. Основной причиной плохого состояния дорожного полотна является несвоевременное обнаружение и ремонт повреждений. Мы предлагаем при помощи автономного дрона выполнять облет дорог, нейросетью обнаруживать ямы и передавать информацию в дорожные службы. А при помощи автономного ровера выполнять ремонт этих ям.

## Описание работы
Квадрокоптер автономно выполняет облет городских улиц и при помощи нейронной сети обнаруживает ямы и дефекты дорожного полотна. Все данные о найденных дефектах отправляются на сервер, который составляет карту повреждений. По ночам, когда автомобилей на дорогах меньше, автономный ровер выезжает на ремонт дороги. Он передвигается по заранее составленному маршруту, соблюдая ПДД, распознавая показания светофоров и прочее. По прибытии на место работ ровер при помощи лидара сканирует яму, определяет ее размер и объем. На основе полученных данных он принимает решение о самостоятельном ремонте либо же передаче информации о том, что эту яму необходимо устранять вручную. Если яма пригодна для автономного ремонта, он подает необходимый объем асфальтобетонной смеси в яму, а затем проезжается по ней, выравнивая ее.
<img src="https://github.com/user-attachments/assets/aef99189-2918-4f31-ac18-a4064c36c16b" width="515" height="431">


## Требования к системе:
- Квадрокоптер должен быть способен автономно выполнять облет городских улиц.
- Нейросеть должна обрабатывать изображение с камеры дрона и распозновать разные ямы.
- Сервер должен составлять карту повреждений на основе данных, полученных от квадрокоптера.
- Сервер должен составлять оптимальный маршрут для ровера
## Задачи проекта
- Подготовить датасет и обучить нейронную сеть на распознавание ям тестовой карты.
- Настроить дрон под работу в автономном режиме. Загрузить и отладить работу нейронной сети на дроне.
- Разработать алгоритм работы с результатами распознавания: подсчет количества ям, определение их координат, передача данных на сервер.
- Разработать серверное приложение с функцией приема данных с дрона, обработке данных о ямах, сборе статистики и передаче информации об обнаруженных ямах пользователям.
- Протестировать систему и внести изменения на основе результатов тестирования.

[**`Реализация проекта`**](https://github.com/ElenaRzh/Autonomous-road-surface-monitoring-and-repair-system./blob/main/DEVELOPMENT.md)
  
[**`Распределение задач`**](https://github.com/user-attachments/files/17155210/Tasks.xlsx)



[**`Порядок выполнения проверок`**](https://github.com/user-attachments/files/17155214/system_test.xlsx)



